<?php
ini_set('display_errors',1);
ini_set('display_startup_errros',1);
error_reporting(E_ALL);
require_once('twitter-api-php/TwitterAPIExchange.php');
require 'vendor/autoload.php';
use Cvuorinen\Raspicam\Raspistill;

/*
cuenta antigua
$settings = array(
    'oauth_access_token' => "2929730890-FzwuPzlQ628VZlehaJXPZexEQEKyOvjG26OEgvG",
    'oauth_access_token_secret' => "7CMdLTuRMwOJ8EFLUkK17c0YP1gGCX26HtyQMcLdU6mmZ",
    'consumer_key' => "ExYUACK1zPYudi1cEoHmk1Mwz",
    'consumer_secret' => "IGJ6tHRVkLZd8vP0xhEyynV5hHp6HVRc9aw66S4XYBmgcRjNQh"
);*/
$settings = array(
    'oauth_access_token' => "WEVTSF9yMjVSN3E1dUFzczRvd1o6MTpjaQ",
    'oauth_access_token_secret' => "Xca2MTzVlu0eelGKfmicaw2r8R4U17MDBlyYuZH_kOqnkohAVy",
    'consumer_key' => "b75xPpzpsdnjf08Yo340mHvbF",
    'consumer_secret' => "N0zOqUzGePVHEu3pJ1OMs1XqWVdhG2bn0lzaaYzpziNQmZXKZb"
);

passthru("raspistill -o pics/test.jpg");

$camera = new Raspistill();
$camera->timeout(1)
	->exposure(Raspistill::EXPOSURE_NIGHT)
	->quality(30);


$path = '/media/usb/camera/picture.jpg';
$camera->takePicture($path);




$url = "https://api.twitter.com/1.1/blocks/create.json";
$requestMethod = 'POST';



$urlIMG = "https://upload.twitter.com/1.1/media/upload.json";

$file = file_get_contents($path);
$data = base64_encode($file);

$postIMG = array(
	'name' => 'test',
	'media_data' => $data
);

$twitter = new TwitterAPIExchange($settings);

$json = $twitter
	->buildOauth($urlIMG, 'POST')
	->setPostfields($postIMG)
	->performRequest();

// Result is a json string
$res = json_decode($json);
// Extract media id
$id = $res->media_id_string;

$twitter = new TwitterAPIExchange($settings);

$url = 'https://api.twitter.com/1.1/statuses/update.json';
$requestMethod = 'POST';
$postfields = array(
	'media_ids' => $id,
	'status' => 'Foto' );

if(strlen($postfields['status']) <= 140)
{
//$twitter = new TwitterAPIExchange($settings);
echo $twitter->buildOauth($url, $requestMethod)
	->setPostfields($postfields)
	->performRequest();
	}else{
		echo "140 char exceed";
	}

?>
<html>
<body>
<img src="pics/picture.jpg">
</body>
</html>
