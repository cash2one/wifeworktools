<?php
/*
 * 功能:
 * 
 */
define("DEBUG_LOGIN", false);
define("DEBUG_FETCHPAGE", false);
define("ASOTMPFILE", "tp.html");

$sheet_header['A1'] = '关键词';
$sheet_header['B1'] = '排名';
$sheet_header['C1'] = '变化';
$sheet_header['D1'] = '数量';
$sheet_header['E1'] = '搜索指数';
$sheet_header['F1'] = '结果数';

$ciarr[] = "兼职";
$ciarr[] = "斗米兼职";
$ciarr[] = "斗米";
$ciarr[] = "找工作软件";
$ciarr[] = "找工作";
$ciarr[] = "兼职招聘";
$ciarr[] = "大学生兼职";
$ciarr[] = "学生兼职";
$ciarr[] = "手机兼职";
$ciarr[] = "网上兼职";
$ciarr[] = "网络兼职";
$ciarr[] = "找兼职";
$ciarr[] = "兼职软件";
$ciarr[] = "实习";
$ciarr[] = "兼职网";
$ciarr[] = "兼职app";
$ciarr[] = "兼职赚钱";
$ciarr[] = "在家兼职";
$ciarr[] = "在家赚钱";
$ciarr[] = "学生赚钱";
$ciarr[] = "小时工";
$ciarr[] = "暑假兼职";
$ciarr[] = "暑期兼职";
$ciarr[] = "暑假工";
$ciarr[] = "周末兼职";
$ciarr[] = "校园兼职";
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
$ciarr[] = "兼職";
$ciarr[] = "兼职工作";
$ciarr[] = "兼职找工作";
$ciarr[] = "大学生兼职网";
$ciarr[] = "兼职猫";
$ciarr[] = "兼职达人";
$ciarr[] = "探鹿";
$ciarr[] = "兼客兼职";
$ciarr[] = "打字兼职";
$ciarr[] = "打字赚钱";
$ciarr[] = "打字";
$ciarr[] = "打字员";
$ciarr[] = "服务员";
$ciarr[] = "送餐";
$ciarr[] = "在线兼职";
$ciarr[] = "兼职在线";
$ciarr[] = "特工任务";
$ciarr[] = "斗米特工";
$ciarr[] = "私活";
$ciarr[] = "下载软件赚钱";
$ciarr[] = "可以赚钱的软件";
$ciarr[] = "兼职圈";
$ciarr[] = "兼职无忧";
$ciarr[] = "投票赚钱";
$ciarr[] = "任务赚钱";
$ciarr[] = "做任务赚钱";
$ciarr[] = "问卷调查";
$ciarr[] = "手机挣钱";
$ciarr[] = "手机赚钱";
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
$ciarr[] = "赶集";
$ciarr[] = "赶集网";
$ciarr[] = "赶集网找工作";
$ciarr[] = "工作软件";
$ciarr[] = "找工作网";
$ciarr[] = "同城招聘";
$ciarr[] = "招聘平台";
$ciarr[] = "招聘";
$ciarr[] = "直聘";

//模拟登录
function aso_login() {
    if (DEBUG_LOGIN)
        return;
    $ch = curl_init();

    $url = "http://aso100.com/account/signinForm";

    $data['username'] = "";
    $data['password'] = "";

    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_HEADER, 1);
    curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookiefile.txt');
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);

    $result = curl_exec($ch);

    curl_close($ch);

    //$result = json_decode($result);
    // if ($result['code'] !="10000")
    //  return false ;

    preg_match_all('/^Set-Cookie:\s*([^;]*)/mi', $result, $matches);
    $cookies = array();

    foreach ($matches[1] as $item) {
        parse_str($item, $cookie);
        $cookies = array_merge($cookies, $cookie);
    }
    return ($cookies);
}

//获取数据页面
function get_asopage($cookies = "") {
    if (DEBUG_FETCHPAGE)
        return true;

    $ch = curl_init();
    $url = "http://aso100.com/app/keyword/appid/1055596148";

    curl_setopt($ch, CURLOPT_URL, $url);

    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_HEADER, 1);
    curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookiefile.txt');

    $result = curl_exec($ch);
    if (curl_errno($ch)) {
        echo 'Curl error: ' . curl_error($ch);
    }

    file_put_contents(ASOTMPFILE, $result);
    curl_close($ch);
    return $result;
}

//从本地文件读取数据
function get_json_byfile($msg = "") {

    $msg = file_get_contents(ASOTMPFILE);
    preg_match_all('/var tableData = (\[\[.*\]\])/mi', $msg, $matches);
    //print_r($matches);
    $str = $matches[1][0];
    //echo $str ;
    $arr = json_decode($str);
    return $arr;
}

//解析数据
function parse_data($arr, $ci) {
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
            $updown = "-";
            if ($updown_num == 0)
                $updown = "#";
        } else {
            $updown = "+";
            $updown_num = $arr_array[1];
        }

        $search_num = $v[2];
        $rs_num = $v[3];

        //名字,排名,+/-,幅度,搜索数,结果指数
        $returnarr[] = array($name, $now_paiming, $updown, $updown_num, $search_num, $rs_num);
    }


    return $returnarr;
}

function out_file($arr) {

    $dir = "data";
    if (!is_dir($dir))
        mkdir($dir);

    $file = $dir . "/" . date("Y-m-d") . ".txt";
    $fp = fopen($file, "w");
    if ($fp) {
        foreach ($arr as $v) {
            fwrite($fp, $v[0] . "_" . $v[1] . "_" . $v[2] . "_" . $v[3] . "_" . $v[4] . "_" . $v[5] . "\r\n");
        }
        fclose($fp);
    }
}

function saveexcel() {

    global $sheet_header;
    global $ciarr;

    set_include_path(get_include_path() . PATH_SEPARATOR . '../Classes/');
    include 'PHPExcel/IOFactory.php';

    $sheet = date("Y-m-d");
    $file = "data/" . date("Ym") . ".xlsx";
    if (!file_exists($file)) {
        $objPHPExcel = new PHPExcel();
        $objWriter = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
        $objWriter->save($file);
        $objPHPExcel = NULL;
        $objWriter = NULL;
    }
 
    copy($file, "data/bak_" . date("Ym") . ".xlsx") ;//备份
    $objPHPExcel = PHPExcel_IOFactory::load($file);
    $objPHPExcel->createSheet();
    $objPHPExcel->setActiveSheetIndex(0);
    $objPHPExcel->getActiveSheet()->setTitle($sheet);

    foreach ($sheet_header as $k => $v) {

        //$objPHPExcel->setActiveSheetIndex(0)
        // ->setCellValue('A1', '关键词')

        $objPHPExcel->setActiveSheetIndex(0)->setCellValue($k, $v);
        $objPHPExcel->getActiveSheet()->getStyle($k)->getAlignment()->setHorizontal(PHPExcel_Style_Alignment::HORIZONTAL_CENTER);
        $objPHPExcel->getActiveSheet()->getStyle($k)->getFont()->setBold(true);
    }

    $fileimport = "data/" . date("Y-m-d") . ".txt";
    $dataarr = file($fileimport);

    $row = 2;
    foreach ($dataarr as $v) {
        $v = trim($v);
        if ($v == "")
            continue;
        $tmpstr = explode("_", $v);

        if (in_array($tmpstr[0], $ciarr)) {

            foreach ($tmpstr as $kk => $vv) {
                $objPHPExcel->getActiveSheet()->setCellValueByColumnAndRow($kk++, $row, $vv);
            }
            $row++;
        }
    }

    $objWriter = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
    $objWriter->save($file);
}

$cookies = aso_login();
$pagestr = get_asopage();
$pagestr = get_json_byfile($pagestr);
$arr = parse_data($pagestr, $ciarr); //解析数据
if (count($arr)<=0) {
    echo date("Y-m-d") . "_error\r\n";
    exit ;
}
out_file($arr);//输出到文本文件
saveexcel();//解析成excel，并备份上一次的文件

