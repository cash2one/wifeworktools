<?php
ini_set("display_errors","On");
error_reporting(E_ALL);
$file = "/usr/share/nginx/proxyinfo.log";
if (is_file($file)) {
        echo file_get_contents($file);
        unlink($file);
}
//print_r(error_get_last());
