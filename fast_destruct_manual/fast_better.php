<?php

function process_object($object)
{
    $key = 7896543210;
    $array = [$key => $object, $key + 1 => $key];
    $serialized = serialize($array);
    return str_replace($key + 1, $key, $serialized);
}

?>
