# UpLoAdEr    

用法：python upload.py 要上传的文件.txt 传输时分块大小 目标文件    

程序是这么运行的：

1.首先把你指定的1.exe通过base64编码生成文本格式的1.txt（这个1.txt你可以通过certutil -decode在目标机上还原1.exe）  
2.将1.txt按照你指定的大小分块，方便不同长度限制下的传输   
3.把第二步得到的分割后的小文件块都拼接上"cmd /c echo .......>2.txt"（2.txt是你指定的目标机器上的文件名）,然后一行一行地保存在当前文件夹下的cmd.txt里面  
	
这样你就可以通过定制自己的payload，循环发包上传文件了，上传后用certutil还原成源文件    
