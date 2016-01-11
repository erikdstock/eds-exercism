<?php

const dnaToRna = array(
    'G' => 'C',
    'C' => 'G',
    'T' => 'A',
    'A' => 'U',
);

function rnaToDna()
{
    return array_flip(dnaToRna);
}

function toRna($dnaString)
{
    $dnaArray = str_split($dnaString);
    $result = "";
    foreach($dnaArray as $char)
    {
        $result = $result . dnaToRna[$char];
    }
    return $result;
}


?>