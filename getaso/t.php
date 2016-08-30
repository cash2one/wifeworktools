<?php

require __DIR__ . '/vendor/autoload.php';

use Nette\Mail\Message;

$mail = new Message;
$mail->setFrom('xyuweido@163.com')
    ->addTo('yaya_8777@163.com')
    ->setSubject('Order Confirmation')
    ->setBody("Hello, Your order has been accepted.");

use Nette\Mail\SendmailMailer;

$mailer = new SendmailMailer;
$mailer->send($mail);
