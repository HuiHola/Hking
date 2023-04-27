<?php 
	$data=file_get_contents("php://input");
	$file=fopen("user_battery.json",'w');
	fwrite($file,$data);
	fclose($file);
?>
