// 文件对象转换问blob地址
function getObjectURL(file) {  
    var url = null;   
    if (window.createObjectURL!=undefined) {  
     url = window.createObjectURL(file) ;  
    } else if (window.URL!=undefined) { // mozilla(firefox)  
     url = window.URL.createObjectURL(file) ;  
    } else if (window.webkitURL!=undefined) { // webkit or chrome  
     url = window.webkitURL.createObjectURL(file) ;  
    }  
    return url ;  
   } ;

//dataURL to blob
function dataURLtoBlob(dataurl) {
    var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
    while(n--){
        u8arr[n] = bstr.charCodeAt(n);
    }
    return new Blob([u8arr], {type:mime});
};

// dataURL to file
function dataURLtoFile(dataurl, filename) {
    var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
    while(n--){
        u8arr[n] = bstr.charCodeAt(n);
    }
    return new File([u8arr], filename, {type:mime});
};


