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
    <form method='post' action='hasil.php' enctype='multipart/form-data'>
        <h2>Selamat Datang!</h2>
        <p>Penerjemahan Bahasa Sunda ke Indonesia atau Indonesia ke Sunda dapat dilakukan dengan memasukkan kalimat dan kamus yang diinginkan ke form yang disediakan. Selamat Mencoba!</p>
        <div class="title" id="bagianIsi">
            <br>
            <br>
            </div>
            <h4 style="text-align: left"><?php echo 'Pilih Kamus'; ?></h3>
            <!--Opsi Kamus yang dapat digunakan-->
            <div class="radio-container">
                <input type="radio" id="Indo-Sunda" name="Kamus" value="Indo-Sunda">
                <label class ="radio" for="Indonesia-Sunda">Indonesia-Sunda</label><br>

                <input type="radio" id="Sunda-Indo" name="Kamus" value="Sunda-Indo">
                <label class ="radio" for="Sunda-Indonesia">Sunda-Indonesia</label><br>
            </div>
            <br>
            <h4 style="text-align: left">Masukkan Kalimat</h3>
            <div class="search-bar">
                <input class="input-box" type = "text" placeholder="Masukan Kalimat" name="Kalimat" >
                <input type="submit" name="submit" value="submit">
            </div>
            <br>
            <br>
        </form>
</div>

<?php include("footer.php");?>

</body>
</html>