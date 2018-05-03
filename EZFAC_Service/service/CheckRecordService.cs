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
        public static void handleFileDate(string ditPath)
        {
         //   WriteLog("开始获取数据:" + ditPath);
            DirectoryInfo dir = new DirectoryInfo(@ditPath);
            FileInfo[] files = dir.GetFiles();
            Check check = null;
            Dictionary<string, string> dic = null;
            for (int i = 0; i < files.Count(); i++)
            {
                WriteLog(files[i].FullName);
                check = CommonUtils.handleFile(files[i]);
                WriteLog("输出数据1:");
                dic = CommonUtils.getDictionary(check);
                WriteLog("输出数据2:");
                foreach (string key in dic.Keys)
                {
                    WriteLog(key + "  ---> " + dic[key]);
                }
                WebHandle.Post("http://192.168.2.149:8800/add-checkRecord", dic);
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
