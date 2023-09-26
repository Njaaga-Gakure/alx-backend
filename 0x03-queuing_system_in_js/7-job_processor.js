import { createQueue } from 'kue';

const queue = createQueue({
  redis: {
    host: 'localhost',
    port: 6379,
  }
});

const blacklistedNumbers = ["4153518780", "4153518781"];
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    job.progress(50, 100);
    done();
  }
}
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});