import { createClient, print } from 'redis';

const client = createClient({
  host: 'localhost',
  port: 6379
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

const obj = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
}

for(const [key, value] of Object.entries(obj)) {
  client.hset('HolbertonSchools', key, value, (_, reply) => {
    print(`Reply: ${reply}`);
  });
}

client.hgetall('HolbertonSchools', (_, reply) => {
  console.log(reply);
});
