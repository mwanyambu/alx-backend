#!/usr/bin/node
/**
 * create job
 */
import { createQueue } from 'kue';

const queue = createQueue();
const jobInfo = { phonenumber: '+1234567890', message: 'Please verify your identification'};

const job = queue
  .create('push_notification_code', jobInfo)
  .save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
  });
job.on('complete', (result) => { /* eslint-disable-line no-unused-vars */
  console.log('Notification job completed');
});
job.on('failed', (err) => { /* eslint-disable-line no-unused-vars */
  console.log('Notification job failed');
});