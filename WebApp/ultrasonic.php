<?php
$file = "ultrasonicStatus.txt";
$handle = fopen($file,'w+');
if (isset($_POST['scan']))
{
$cmdstring = "scan";
fwrite($handle,$cmdstring);
fclose($handle);
print "
<!DOCTYPE html>
<html lang='en'>
<head>
<title>Raspberry pi</title>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>
  <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
  <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script>
<body align='center'>
<title>Lextor Control Unit</title>

<h2 style='background:green'>Ultrasonic is Running</h2>
</body>
</html>
";
}
if (isset($_POST['stop']))
{
$cmdstring = "stop";
fwrite($handle,$cmdstring);
fclose($handle);
print "
<!DOCTYPE html>
<html lang='en'>
<head>
<title>Raspberry pi</title>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>
  <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
  <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script>
<body align='center'>
<title>Lextor Control Unit</title>

<h2 style='background:green'>Ultrasonic has Stopped</h2>
</body>
</html>
";
}
?>