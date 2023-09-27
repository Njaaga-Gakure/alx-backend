import { createClient } from 'redis';
import { promisify } from 'util';
import { createQueue } from 'kue';
import express from "express";


const client = createClient({
  host: 'localhost',
  port: 6379
});
const getAsync = promisify(client.get).bind(client);
const queue = createQueue();

client.on('connect', () => {
  console.log('Redis client connected to the server');
})
.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});


const reserveSeat = (number) => {
  client.set('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const availableSeats = await getAsync('available_seats');
  return availableSeats;
};

reserveSeat(50);
let reservationEnabled = true;

const app = express();
const port = 1245;

app.get('/available_seats', async (_, res) => {
   const numberOfAvailableSeats = await getCurrentAvailableSeats();
   res.status(200).json({ numberOfAvailableSeats })
});


app.get('/reserve_seat', (_, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' })
    return;
  }
  const jobData = {};
  const job = queue.create('reserve_seat', jobData);
  job.save((err) => {
    if (err) {
      res.json({ status: "Reservation failed" });
      return;
    }
      res.json({ status: "Reservation in process" });
  });
  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`)
  });
  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

app.get('/process', (_, res) => {
  queue.process('reserve_seat', async (job, done) => {
     let numberOfAvailableSeats = await getCurrentAvailableSeats();
     numberOfAvailableSeats = numberOfAvailableSeats - 1;
     reserveSeat(numberOfAvailableSeats);
     if (numberOfAvailableSeats == 0) {
       reservationEnabled = false;
     }
     if (numberOfAvailableSeats < 0) {
       done(new Error('Not enough seats available'));
     }
     done();
  });
  res.json({ status: "Queue processing" })
});

app.listen(port, () => {
  console.log(`Server listen on port ${port}...`)
});
