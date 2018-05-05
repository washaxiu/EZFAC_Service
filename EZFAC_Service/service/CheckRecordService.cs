using EZFAC_Service.Common;
using EZFAC_Service.model;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EZFAC_Service.service
{
    class CheckRecordService
    {
        public static void handleFileDate(string ditPath,string url)
        {
         //   WriteLog("开始获取数据:" + ditPath);
            DirectoryInfo dir = new DirectoryInfo(@ditPath);
            FileInfo[] files = dir.GetFiles();
            Check check = null;
            Dictionary<string, string> dic = null;
            for (int i = 0; i < files.Count(); i++)
            {
           //     WriteLog(files[i].FullName);
                if (files[i].Extension.Equals(".ykk"))       // 判断是否为ykk文件
                {
                    check = CommonUtils.handleFile(files[i]);
                    dic = CommonUtils.getDictionary(check);
                    foreach (string key in dic.Keys)
                    {
                        WriteLog(key + "  ---> " + dic[key]);
                    }
                    WebHandle.Post(url, dic);
                }
              //  WriteLog(dic.Keys.ToList().ToString());
            }
        }

        public static void WriteLog(string msg)
        {
            //该日志文件会存在windows服务程序目录下
            string path = @"e:\log\";
            path += DateTime.Now.Year + "_" + DateTime.Now.Month + "_access_log.txt";
            FileInfo file = new FileInfo(path);
            if (!file.Exists)
            {
                FileStream fs;
                fs = File.Create(path);
                fs.Close();
            }

            using (FileStream fs = new FileStream(path, FileMode.Append, FileAccess.Write))
            {
                using (StreamWriter sw = new StreamWriter(fs))
                {
                    sw.WriteLine(DateTime.Now.ToString() + "   " + msg);
                }
            }
        }
    }
}
