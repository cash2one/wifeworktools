<?php

/*
 * 34 11 * * * root cd /code/PHPExcel/aso && /usr/bin/php /code/PHPExcel/aso/getaso.php >>/code/PHPExcel/aso/error.log 2
  >&1
 * 
 */
define('ROOT', __DIR__ );

include ROOT . DIRECTORY_SEPARATOR . 'PHPExcel-1.8/Classes/PHPExcel/IOFactory.php';

define("DEBUG_LOGIN", true);
define("DEBUG_FETCHPAGE", true);

define("PRODATA", ROOT . DIRECTORY_SEPARATOR . 'asodata');

define("COOKIEYZM", PRODATA . DIRECTORY_SEPARATOR . 'cookiefileyzm.txt'); //代表读取验证码生成的cookie
define("COOKIEUSER", PRODATA . DIRECTORY_SEPARATOR . 'cookiefile.txt'); //等表登录后生成的cookie

define("YZMIMGSRC", PRODATA . DIRECTORY_SEPARATOR . "yzmsrc.png");
define("YZMIMGDESC", PRODATA . DIRECTORY_SEPARATOR . "yzmdesc.png");

//假如手动运行,可以替换该常量
define("ASOFILEFIX", date("Y-m-d-H"));

define("ASOTMPFILE", PRODATA . DIRECTORY_SEPARATOR . ASOFILEFIX . '.html'); //读取的模版文件
define("ASOOUTFILE", PRODATA . DIRECTORY_SEPARATOR . ASOFILEFIX . '.txt'); //生成的文本文件

define("XLSFILE", PRODATA . DIRECTORY_SEPARATOR . date("Ym") . ".xlsx");//xls文件,每个月一个文件


define("LOGFILE", PRODATA . DIRECTORY_SEPARATOR . "record.txt");

$header[] = 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36';
$header[] = 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8';
//$header[] = "Accept-Encoding:gzip, deflate, sdch";
$header[] = "Accept-Language:zh-CN,zh;q=0.8,en;q=0.6";

$sheet_header['A1'] = '关键词';
$sheet_header['B1'] = '搜索指数';
$sheet_header['C1'] = '排名';
$sheet_header['D1'] = '变化';


$ciarr[] = "兼职";
$ciarr[] = "斗米兼职";
$ciarr[] = "斗米";
$ciarr[] = "斗米特工";
$ciarr[] = "特工任务";
$ciarr[] = "兼职app";
$ciarr[] = "兼职网";
$ciarr[] = "兼职赚钱";
$ciarr[] = "手机兼职";
$ciarr[] = "找工作软件";
$ciarr[] = "找工作";
$ciarr[] = "兼职招聘";
$ciarr[] = "学生兼职";
$ciarr[] = "大学生兼职";
$ciarr[] = "兼职软件";
$ciarr[] = "网上兼职";
$ciarr[] = "网络兼职";
$ciarr[] = "找兼职";
$ciarr[] = "实习";
$ciarr[] = "在家兼职";
$ciarr[] = "在家赚钱";
$ciarr[] = "学生赚钱";
$ciarr[] = "暑假兼职";
$ciarr[] = "暑期兼职";
$ciarr[] = "暑假工";
$ciarr[] = "家教";
$ciarr[] = "家教兼职";
$ciarr[] = "模特兼职";
$ciarr[] = "宝妈兼职";
$ciarr[] = "淘宝兼职";
$ciarr[] = "北京兼职";
$ciarr[] = "上海兼职";
$ciarr[] = "深圳兼职";
$ciarr[] = "广州兼职";
$ciarr[] = "附近兼职";
$ciarr[] = "周末兼职";
$ciarr[] = "校园兼职";
$ciarr[] = "兼職";
$ciarr[] = "兼职猫";
$ciarr[] = "兼职达人";
$ciarr[] = "探鹿";
$ciarr[] = "兼客兼职";
$ciarr[] = "靠谱兼职";
$ciarr[] = "在线兼职";
$ciarr[] = "兼职在线";
$ciarr[] = "线上兼职";
$ciarr[] = "兼职工作";
$ciarr[] = "兼职找工作";
$ciarr[] = "大学生兼职网";
$ciarr[] = "小时工";
$ciarr[] = "打字兼职";
$ciarr[] = "打字赚钱";
$ciarr[] = "打字";
$ciarr[] = "打字员";
$ciarr[] = "服务员";
$ciarr[] = "送餐";
$ciarr[] = "私活";
$ciarr[] = "任务赚钱";
$ciarr[] = "做任务赚钱";
$ciarr[] = "做任务";
$ciarr[] = "下载软件赚钱";
$ciarr[] = "可以赚钱的软件";
$ciarr[] = "能赚钱的软件";
$ciarr[] = "兼职圈";
$ciarr[] = "兼职无忧";
$ciarr[] = "投票赚钱";
$ciarr[] = "问卷调查";
$ciarr[] = "手机挣钱";
$ciarr[] = "手机赚钱";
$ciarr[] = "手机免费赚钱";
$ciarr[] = "网上赚钱";
$ciarr[] = "网络赚钱";
$ciarr[] = "赚钱网";
$ciarr[] = "赚钱";
$ciarr[] = "赚钱软件";
$ciarr[] = "赚钱神器";
$ciarr[] = "挣钱";
$ciarr[] = "挣钱软件";
$ciarr[] = "打工";
$ciarr[] = "打工赚钱";
$ciarr[] = "58app";
$ciarr[] = "58兼职";
$ciarr[] = "58同城";
$ciarr[] = "五八同城";
$ciarr[] = "58同城网";
$ciarr[] = "58找工作";
$ciarr[] = "附近找工作";
$ciarr[] = "附近工作";
$ciarr[] = "赶集";
$ciarr[] = "赶集网";
$ciarr[] = "赶集网找工作";
$ciarr[] = "工作软件";
$ciarr[] = "找工作网";
$ciarr[] = "同城招聘";
$ciarr[] = "招聘平台";
$ciarr[] = "求职";
$ciarr[] = "招聘";
$ciarr[] = "直聘";
$ciarr[] = "校园招聘";
$ciarr[] = "上海招聘";
$ciarr[] = "求职招聘";
$ciarr[] = "企业招聘";

function parseimg($argv) {
    $filename = $argv[0];
    $descfile = $argv[1];

// 获取新的尺寸
    list($width, $height) = getimagesize($filename);
    $new_width = 66;
    $new_height = 18; //18
// 重新取样
    $image_p = imagecreatetruecolor($new_width, $new_height);
    $image = imagecreatefrompng($filename);

    imagecopy($image_p, $image, 0, 0, 13, 6, $new_width, $new_height);
//imagecopy($image_p, $image, 0, 0, 13, 6, $new_width, $new_height);
    imagepng($image_p, $descfile);
}

//读取验证码并生成一张图片
function aso_yzm() {
    global $header;
    $url = "http://aso100.com/account/getVerifyCodeImage";
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);

    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_BINARYTRANSFER, 1);
    curl_setopt($ch, CURLOPT_REFERER, "http://aso100.com/account/signin");
    curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    // curl_setopt($ch, CURLOPT_COOKIEJAR, 'asodata/cookiefileyzm.txt');

    curl_setopt($ch, CURLOPT_COOKIEJAR, COOKIEYZM);

    $result = curl_exec($ch);
    curl_close($ch);
    file_put_contents(YZMIMGSRC, $result);

    parseimg(array(YZMIMGSRC, YZMIMGDESC));
}

//
function check_yzm() {
    require_once 'Image.class.php';
    $image = new \ImageOCR\Image();
    $image->init(YZMIMGDESC);
    $a = $image->find();
    //$image->draw();
    $code = implode("", $a);
    return $code;
}

function asoyzm_login($code) {
    global $header;

    $ch = curl_init();

    $url = "http://aso100.com/account/signinForm";
    $data['username'] = "";
    $data['password'] = "";
    $data['code'] = $code;
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_REFERER, "http://aso100.com/account/signin");
    // curl_setopt($ch, CURLOPT_USERAGENT,$header['User-Agent']);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    curl_setopt($ch, CURLOPT_COOKIEJAR, COOKIEUSER);
    curl_setopt($ch, CURLOPT_COOKIEFILE, COOKIEYZM);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);

    foreach ($header as $k => $v) {
        // curl_setopt($ch, $k, $v);
    }
    $result = curl_exec($ch);
    curl_close($ch);
    $arr = json_decode($result, true);
    if ($arr['code'] == 10000)
        return TRUE;

    return FALSE;
}

function get_json_byfile() {

    $msg = file_get_contents(ASOTMPFILE);
    preg_match_all('/var tableData = (\[\[.*\]\])/mi', $msg, $matches);
    $str = $matches[1][0];
    if ($str == "")
        RETURN FALSE;
    $arr = json_decode($str);
    return $arr;
}

function get_asopage($cookies = "") {
    global $header;

    $referurl = "http://aso100.com/app/rank/appid/1055596148";
    $ch = curl_init();
    $url = "http://aso100.com/app/keyword/appid/1055596148";
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_HEADER, 1);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
    curl_setopt($ch, CURLOPT_REFERER, $referurl);
    curl_setopt($ch, CURLOPT_COOKIEFILE, COOKIEUSER);
    $result = curl_exec($ch);
    if (curl_errno($ch)) {
        echo 'Curl error: ' . curl_error($ch);
    }
    curl_close($ch);
    file_put_contents(ASOTMPFILE, $result);
    return $result;
}

function out_file($arr) {


    $fp = fopen(ASOOUTFILE, "w");
    if ($fp) {
        foreach ($arr as $v) {
            $str = $v[0] . "_" . $v[4] . "_" . $v[1] . "_" . $v[2] . $v[3] . "\r\n";
            fwrite($fp, $str);
        }
        fclose($fp);
    }
}

//解析数据
//解析数据
function parse_data($arr) {
    /*
      [0] => 兼职在线
      [1] => 1#-0
      [2] => 51
      [3] => 1082
      [4] => 0
      [5] => jzzx
      [6] => 29698
     */
    $returnarr = array();
    foreach ($arr as $k => $v) {
        $arr_1 = $v[1];
        $name = $v[0];
        $arr_array = explode("#", $arr_1);
        $now_paiming = $arr_array[0];
        $arr_updown = $arr_array[1][0];
        if ($arr_updown == "-") {
            $updown_num = substr($arr_array[1], 1, strlen($arr_array[1]) - 1);
            $updown = "下降";
            if ($updown_num == 0)
                $updown = "";
        } else {
            $updown = "上升";
            $updown_num = $arr_array[1];
        }
        $search_num = $v[2];
        $rs_num = $v[3];

        //名字,排名,+/-,幅度,搜索数,结果指数
        $returnarr[] = array($name, $now_paiming, $updown, $updown_num, $search_num, $rs_num);
    }
    return $returnarr;
}

function saveexcel() {

    global $sheet_header;
    global $ciarr;

    $sheet = ASOFILEFIX;
    $file = XLSFILE;
    if (!file_exists($file)) {
        $objPHPExcel = new PHPExcel();
        $objWriter = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
        $objWriter->save($file);
        $objPHPExcel = NULL;
        $objWriter = NULL;
    }

    //copy($file, "asodata/bak_" . date("Ym") . ".xlsx"); //备份
    $objPHPExcel = PHPExcel_IOFactory::load($file);
    $count = $objPHPExcel->getSheetCount();
    $objPHPExcel->createSheet();
    $objPHPExcel->setActiveSheetIndex($count);
    $objPHPExcel->getActiveSheet()->setTitle($sheet);

    foreach ($sheet_header as $k => $v) {

        //$objPHPExcel->setActiveSheetIndex(0)->setCellValue('A1', '关键词')
        $objPHPExcel->getActiveSheet()->setCellValue($k, $v);
        $objPHPExcel->getActiveSheet()->getStyle($k)->getAlignment()->setHorizontal(PHPExcel_Style_Alignment::HORIZONTAL_CENTER);
        $objPHPExcel->getActiveSheet()->getStyle($k)->getFont()->setBold(true);
    }


    $dataarr = file(ASOOUTFILE);

    $row = 2;
    foreach ($dataarr as $v) {

        $v = trim($v);
        if ($v == "")
            continue;
        $tmpstr = explode("_", $v);
        $clarr[$tmpstr[0]] = $tmpstr;
    }
    foreach ($ciarr as $k => $v) {
        if (is_array($clarr[$v])) {
            foreach ($clarr[$v] as $kk => $vv) {
                $objPHPExcel->getActiveSheet()->setCellValueByColumnAndRow($kk++, $row, $vv);
            }
            $row++;
        }
    }

    $objWriter = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
    $objWriter->save($file);
}

function recordlog($msg) {
    $fp = fopen(LOGFILE, "a");
    $str = date("Y-m-d-H:i:s") . "_" . $msg . "\r\n";
    echo $str;
    fwrite($fp, $str);
    fclose($fp);
}

////////////////////////////////////

if (!is_dir(PRODATA))
mkdir(PRODATA);
sleep(100,1000);
recordlog("开始");
get_asopage();
$pagestr = get_json_byfile();

if (!$pagestr) {
    recordlog("没有登陆");
    $sign = FALSE;
    $n = 1;
    while (!$sign) {
	if ($n>15)
		break;
        aso_yzm(); //下载验证码图片
        $code = check_yzm(); //读取验证码
        $sign = asoyzm_login($code);
        recordlog("分析验证码" . $code . "_" . $n);
	$n++;
    }

    get_asopage();
    $pagestr = get_json_byfile();
}


if (!$pagestr) {
    recordlog("解析错误" . $code);
} else {

    $arr = parse_data($pagestr);
    out_file($arr);
    saveexcel();
    recordlog("解析成功");
}
recordlog("结束");


