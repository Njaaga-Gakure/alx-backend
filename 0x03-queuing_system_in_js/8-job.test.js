import createPushNotificationsJobs from './8-job.js';
import { createQueue } from 'kue';
import { expect } from 'chai';

const queue = createQueue();


describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    queue.testMode.enter();
  });
  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });
  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });
  it('should save job to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      },
      {
        phoneNumber: '4153518743',
        message: 'This is the code 4321 to verify your account'
      }
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(3);
  });
  it('should listen for completion, failed and progress events', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      },
      {
        phoneNumber: '4153518743',
        message: 'This is the code 4321 to verify your account'
      }
    ];
    createPushNotificationsJobs(jobs, queue);
    queue.testMode.jobs.forEach((job) => {
      expect(job.listenerCount('complete')).to.equal(1);
      expect(job.listenerCount('failed')).to.equal(1);
      expect(job.listenerCount('progress')).to.equal(1);
    });
  });
});
