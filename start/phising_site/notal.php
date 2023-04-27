<?php 
	$data=file_get_contents("php://input");
	$file=fopen("pernot.txt",'w');
	fwrite($file,$data);
	fclose($file);
?>
