<?php 

$t = '';
$ID = '';
$que = '';
$url = '';


if(isset($_GET['t']))
{
    $t = $_GET['t'];
    if(isset($_GET['id']))
    {
        $ID = $_GET['id'];
        $d = '';
        if($t == 'm')
        {
            $d = 'picm';
        } else if($t == 'pc') {
            $d = 'picpc';
        } else {
            exit('No Permission');
        }

        if(is_numeric($ID))
        {
            // 向数据库查询，并返回一个json
            # 连接数据库
            $mysqli = new mysqli("localhost", "picSpider", "123456", "picSpider");
            # 取出该id
            $sql = "SELECT * FROM " . $d . " WHERE id = ".$ID;
            # 获得当前类型的总数并生成随机数
            $result = $mysqli->query($sql);
            $row = $result->fetch_assoc();
            $arr = array('sus' => 'false');
            if(isset($row['URL'])){
                $arr = array('sus' => 'true', 'id' => $ID, 'originalID' => $row['originalID'], 'URL' => $row['URL']);
            }
            echo json_encode($arr);
            $mysqli->close(); 
        }else if($ID=='all'){
            if($t == 'm')
            {
                $url = '/picture/m/';
                $que = 'numOfMobile';
            } else if($t == 'pc') {
                $url = '/picture/pc/';
                $que = 'numOfPC';
            } else {
                exit('No Permission');
            }
    
            # 连接数据库
            $mysqli = new mysqli("localhost", "picSpider", "123456", "picSpider");
            # 取出最新的信息
            $sql = "select * from atr order by id desc limit 1";
            # 获得当前类型的总数并生成随机数
            $result = $mysqli->query($sql);
            $row = $result->fetch_assoc();
            # 返回数量
            $arr = array('s' => $row[$que]);
            echo json_encode($arr);
            # 关闭数据库
            $mysqli->close();
        }else
        {
            exit('No Permission');
        }


    }else
    {
        if($t == 'm')
        {
            $url = '/picture/m/';
            $que = 'numOfMobile';
        } else if($t == 'pc') {
            $url = '/picture/pc/';
            $que = 'numOfPC';
        } else {
            exit('No Permission');
        }

        # 连接数据库
        $mysqli = new mysqli("localhost", "picSpider", "123456", "picSpider");
        # 取出最新的信息
        $sql = "select * from atr order by id desc limit 1";
        # 获得当前类型的总数并生成随机数
        $result = $mysqli->query($sql);
        $row = $result->fetch_assoc();
        $randomNum = (string)mt_rand(1,$row[$que]);
        # 返回图片
        $url = $url.$randomNum.'.webp';
        header('Content-type:image/jpeg');
        Header("HTTP/1.1 302");
        Header("Location: $url"); 
        # 关闭数据库
        $mysqli->close();
    }
}else{
    exit('No Permission');
}

exit;  
?>