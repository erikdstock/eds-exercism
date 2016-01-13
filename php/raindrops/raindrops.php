<?php
function raindrops($number) {
  // $string = strval($number);
  // $length = strlen($string);
  $drops = "";
  $code = array(
    3 => "Pling",
    5 => "Plang",
    7 => "Plong"
  );

  // for ($i = 0; $i <= $length; $i++)
  // {
    // $char = substr($string, $i, 1);
    $dropped = false;
    foreach ($code as $factor => $sound)
    {
        if ($number / $factor > 0 and $number % $factor == 0)
        {
          $dropped = true;
          $drops .= $sound;
        }
    }
    if (!$dropped)
    {
      $drops .= $number;
    }
  // }
  return $drops;
}
?>
