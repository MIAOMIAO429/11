#找文件
import os



def test_OS():
    print(os.listdir("递归测试"))  #列出路径下内容
    print(os.path.isdir("递归测试/1.2"))#判断指定路径是不是文件夹
    print(os.path.exists("递归测试"))#判断指定路径是否存在

def get_files_recursion_form_dir(path):  #遍历文件
    #从指定文件夹中使用递归方法 获取全部文件列表
    #prarm path 被判断的文件夹
    #return ：list 包含全部文件  如果目录不存在/无文件 返回空列表（list）
    file_list=[]
    print(f"当前判断文件夹是：{path}")
    if os.path.exists(path):
        for x in os.listdir(path):
          new_path=path+"/"+x
          if os.path.isdir(new_path):#终止条件
              file_list += get_files_recursion_form_dir(new_path)
          else:
              file_list.append(new_path)
                #进入这里 表明目录文件夹不是文件

    else:
        print(f"指定目录{path}不存在")
        return []

    return file_list
if __name__ == '__main__':
   print(get_files_recursion_form_dir('递归测试'))