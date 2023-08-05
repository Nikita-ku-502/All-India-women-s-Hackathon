<!-- PHP code for generating a captcha image -->
<?php
session_start();
$captcha = generateCaptcha();
$_SESSION['captcha'] = $captcha;

header('Content-Type: image/png');
$image = imagecreatetruecolor(150, 50);
$bgColor = imagecolorallocate($image, 255, 255, 255);
$textColor = imagecolorallocate($image, 0, 0, 0);
imagefilledrectangle($image, 0, 0, 150, 50, $bgColor);
imagettftext($image, 20, 0, 10, 35, $textColor, 'path/to/font.ttf', $captcha);
imagepng($image);
imagedestroy($image);

function generateCaptcha() {
  $characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  $captcha = '';
  for ($i = 0; $i < 6; $i++) {
    $captcha .= $characters[rand(0, strlen($characters) - 1)];
  }
  return $captcha;
}
?>
