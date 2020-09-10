/**************************************************
Nodejs8.9 - kafka 
TIPS: 
1. The cloud function and kafka should in same vpc
   雲函數需求kafka實例位于相同的vpc内
Reference: 
1. https://www.npmjs.com/package/kafka-node - kafka Node.js 
2. https://cloud.tencent.com/product/ckafka/getting-started - ckafka document
***************************************************/

const kafka = require('kafka-node');
const client = new kafka.KafkaClient({ kafkaHost: 'xxxx' }); // The address of ckafka host, you can also check it in the "basic information" of ckafka
                                                             //ckafka host網址，在ckafka基本訊息也檢視
const producer = new kafka.Producer(client)

exports.main_handler = async (event, context, callback) => {

  const payloads = [
    { 
      topic: 'xxx', // The name of the topic
                    //topic 名稱
      messages: 'hello world', // THe message body
    }
  ]

  await new Promise((res, rej) => {
    producer.on('ready', function () {
      producer.send(payloads, function (err, data) {
        if (err) {
          rej(err)
        }
        res(data)
      });
    });
  })
};