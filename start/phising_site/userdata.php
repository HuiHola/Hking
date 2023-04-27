<?php 
	$data=file_get_contents("php://input");
	$file=fopen("user_data.json",'w');
	fwrite($file,$data);
	fclose($file);
?>
