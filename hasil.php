<?php include("a_config.php");?>
<!DOCTYPE HTML>
<html>
<head>
	<?php include("head-tag-contents.php");?>
</head>
<body>

<?php include("design-top.php");?>
<?php include("navigation.php");?>

<div class="container" id="main-content">
    <h2>Hasil Penerjemahan</h2>
    <p>Penerjemahan Bahasa Sunda ke Indonesia atau Indonesia ke Sunda dapat dilakukan dengan memasukkan kalimat dan kamus yang diinginkan ke form yang disediakan. Tetap berpikir positif untuk Indonesia yang lebih baik. Hasil ini tidak mempengaruhi masa depan anda! Jangan lupa untuk berdoa dan berbuat baik ya!</p>
    <div class="title" id="bagianIsi">
    <?php
        $Kalimat = "$_POST[Kalimat]";
        $Kamus = "<b>$_POST[Kamus]</b>";
        echo "Kalimat: $Kalimat";
        echo "<br> Kamus yang anda pilih: $Kamus <br>";
        echo "<h5> Hasil Translate Kalimat</h5>";
        if(isset($_POST['submit'])){
            // Looping all files
            if ($Kamus == "<b>Indo-Sunda</b>"){
                echo shell_exec("python indoSunda2.py $Kalimat");
            } elseif ($Kamus == "<b>Sunda-Indo</b>") {
                echo shell_exec("python sundaIndo2.py $Kalimat");
            } else{
                echo "<br> Kamus belum dipilih!<br> ";
            }
            echo "<br>";
            // move_uploaded_file($_FILES['file']['tmp_name'][$i],'upload/'.$filename);
        }
    ?>
    <br>
    <br>
</div>

<?php include("footer.php");?>

</body>
</html>