import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient({
  host: 'localhost',
  port: 6379
});
const getAsync = promisify(client.get).bind(client);
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      print(`Reply: ${err}`)
    } else {
      print(`Reply: ${reply}`)
    }
  });
};

const displaySchoolValue = async (schoolName) => {
  const value = await getAsync(schoolName);
  console.log(value);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
