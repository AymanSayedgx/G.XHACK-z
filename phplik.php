<?php
require 'vendor/autoload.php';

use GuzzleHttp\Client;

function generate_username() {
    $letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $digits = '0123456789';
    $username_letters = substr(str_shuffle($letters), 0, 10);
    $username_digits = substr(str_shuffle($digits), 0, 5);
    return $username_letters . $username_digits;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $User = generate_username();
    $link = $_POST['link'];

    $client = new Client();
    $response = $client->post('https://api.likesjet.com/freeboost/7', [
        'json' => [
            'email' => 'hackyourdata' . rand(100000, 999999) . '@gmail.com',
            'link' => $link,
            'instagram_username' => $User
        ],
        'headers' => [
            'accept-language' => 'en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'referer' => 'https://likesjet.com/',
            'sec-fetch-dest' => 'empty',
            'sec-fetch-mode' => 'cors',
            'sec-fetch-site' => 'same-site',
            'origin' => 'https://likesjet.com',
            'sec-ch-ua-platform' => '"Android"',
            'user-agent' => 'Your-User-Agent-Here', // استبدل هذا بالسلسلة الصحيحة
            'sec-ch-ua-mobile' => '?1',
            'content-type' => 'application/json',
            'accept' => 'application/json, text/plain, */*',
            'sec-ch-ua' => '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'content-length' => '137',
            'Host' => 'api.likesjet.com'
        ]
    ]);

    $body = $response->getBody();
    $data = json_decode($body, true);
    echo $data['message'];
}
?>
