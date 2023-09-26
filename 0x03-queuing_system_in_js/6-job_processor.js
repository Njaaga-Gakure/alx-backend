import { createQueue } from 'kue';

const queue = createQueue({
  redis: {
    host: 'localhost',
    port: 6379,
  }
});

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
