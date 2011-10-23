<?php
	$locations = $_POST['coords'];
	$coords = explode(':',$locations);
	for($i=0 ; $i<count($coords) ; $i++) {
		echo($coords[$i]);
		echo('<br>');
	}	


?>
