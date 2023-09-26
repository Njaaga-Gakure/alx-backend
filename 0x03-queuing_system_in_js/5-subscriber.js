import { createClient } from 'redis';

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

const channelName = 'holberton school channel';

client.subscribe(channelName);
client.on('message', (channel, message) => {
  if (channel === channelName) {
    console.log(message);
    if (message === 'KILL_SERVER') {
      client.unsubscribe(channelName, () => {
        client.quit();
      });
    }
  }
});
