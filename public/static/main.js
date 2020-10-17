/* 
    method
    url
    data
    success  数据下载成功以后执行的函数
    error    数据下载失败以后执行的函数
*/
function $ajax({ method = "get", url, data, success, error }) {
    //1、创建ajax对象
    var xhr = null;
    try {
        xhr = new XMLHttpRequest();
    } catch (error) {
        xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }

    //判断如果数据存在
    if (data) {
        data = querystring(data);
    }

    if (method == "get" && data) {
        url += "?" + data;
    }

    console.log(url)
    xhr.open(method, url, true);

    if (method == "get") {
        xhr.send();
    } else {
        //必须在send方法之前，去设置请求的格式
        xhr.setRequestHeader("content-type", "application/x-www-form-urlencoded");
        xhr.send(data);
    }
    //4、等待数据响应  
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            //判断本次下载的状态码都是多少
            if (xhr.status == 200) {
                /* 
                    如何去处理数据操作不确定
                    回调函数
                */
                if (success) {
                    // alert(2);
                    success(xhr.responseText);
                }
            } else {
                if (error) {
                    error("Error:" + xhr.status);
                }
            }
        }
    }
}

function querystring(obj) {
    var str = "";
    for (var attr in obj) {
        str += attr + "=" + obj[attr] + "&";
    }
    return str.substring(0, str.length - 1);
}

function $(obj) {
    return document.getElementById(obj);
}


// inputID: 表单的id
// inputType: 表单的类型
// sub: 提交表单
// showUrl: 展示链接
// aurl: 链接
// acopy: 复制链接
// inputError: 输入错误
// fatalError: 致命错误


/*
 *	检查当前表单是否合法
 */
var res = ['showUrl', 'inputError', 'fatalError', 'NoFoundError'];

function clear(){
    for(i of res){
        $(i).style.display = 'none';
    }
}

function check(){
    if (  $("inputID").value.length > 0 && ( /^\d+$/.test($("inputID").value)) ) {
        return true;
    } else if( $("inputID").value.length == 0 ){
        return false
    } else {
        $(res[1]).style.display = 'inherit';
        return false;
    }
}

function fatal(){
    $(res[2]).style.display = 'inherit';
}

function NoFound() {
    $(res[3]).style.display = 'inherit';
}

// 按下submit
function subm(){
    clear();
    if(!check()) return;
    $('loading').style.display = 'flex';
    $ajax({
        method: "get",
        url: "https://hk.20021110.xyz/api.php",
        data: {
            id: $("inputID").value,
            t: $("inputType").options[$("inputType").selectedIndex].value
        },
        // 后端返回 JOSON
        // 1. sus 是否成功插入
        // 2. message 插入成功后的信息
        success: function(result) {
            $('loading').style.display = 'none';
            var obj = JSON.parse(result);
            if (obj.sus == "true") {
                $("OURL").value = obj.URL;
                $(res[0]).style.display = 'inherit';
            } else {
                NoFound();
            }

        },
        error: function(msg) {
            $('loading').style.display = 'none';
            fatal();
        }
    })
}

// 复制
function acopy(copyTxt)
{
    $('OURL').select();
    document.execCommand("Copy"); // 执行浏览器复制命令
    alert('复制成功')
}

