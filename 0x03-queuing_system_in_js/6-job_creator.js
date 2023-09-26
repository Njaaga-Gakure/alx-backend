import { createQueue } from 'kue';

const queue = createQueue({
  redis: {
    host: 'localhost',
    port: 6379,
  }
});

const jobData = {
  phoneNumber: '+1 234 5678',
  message: 'sample message',
}

const job = queue.create('push_notification_code', jobData);

job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
});
job.on('failed', () => {
  console.log('Notification job failed');
});
