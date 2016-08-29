<?php

/*
 * 图片ocr
 * 参数 a:空代表根据图片读出数字,否则代表训练
 * 参数 s:代表图片的名字(不包括.png)
 */
require_once 'Image.class.php';


$image = new \ImageOCR\Image( );
$action = $_GET['a'];
$code = $_GET['s'];

$action = ($action==""?$argv[1]:$action);
$code = ($code==""?$argv[2]:$code);

if ($action == "")
	exit("action empty");

if ($code == "")
	exit("code empty");


$image->init("./" . $code . ".png");

//根据图片读出数字
if ($action == "parse") {
    $a = $image->find();
    $image->draw();
    $code = implode("", $a);
    echo "验证码：$code \n";
} else {
  //训练图片
    $code_arr = str_split($code);
    for ($i = 0; $i < $image::CHAR_NUM; $i++) {
        $hash_img_data = implode("", $image->splitImage($i));
 
        if ($hash_img_data != "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111") {
            echo $code_arr[$i] . "_" . $hash_img_data . "<br>";
            //$db->add($code_arr[$i],$hash_img_data);
            $image->adddatatofile($code_arr[$i], $hash_img_data);
        }
    }
    $image->draw();
}

