using EZFAC_Service.model;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EZFAC_Service.Common
{
    class CommonUtils
    {
        public static string[] name = { "name1", "name2", "name3", "name4", "name5" };
        public static string[] date = { "date1", "date2", "date3", "date4", "date5" };
        public static string[] comments = { "comments1", "comments2", "comments3", "comments4", "comments5" };

        //  将文件的信息转化成相应的类
        public static Check handleFile(FileInfo file)
        {
            StreamReader myStreamReader = new StreamReader(file.FullName);    // 读取文件数据
            string content = myStreamReader.ReadToEnd().Replace("   ", "").Replace("\"", "").Replace(",", "");
            
            string[] str = content.Split('\n');
            string[] st = null;
            List<string> checkInfoList = new List<string>();
            List<string> checkContentList = new List<string>();
            List<string> checkerInfoList = new List<string>();
            checkInfoList.Add(file.Name);
            int count = 0;
            for (int i = 0; i < str.Count(); i++)
            {
                if (str[i].IndexOf(":") != -1)
                {
           //         WriteLog("文件内容:" + str[i]);
                    st = str[i].Trim().Split(':');
                    // 以[ 为 每段的结束点
                    if (st[1].Equals("["))
                    {
                        count++;
                        continue;
                    }
                    if (count == 1)
                    {
                        checkInfoList.Add(st[1]);
                    }
                    else if (count == 2)
                    {
                        checkContentList.Add(st[1]);
                    }
                    else if(count == 3)
                    {
                        checkerInfoList.Add(st[1]);
                    }
                }
            }
            // 设置 文件中  checkInfo 的内容 ，并加上文件名
            CheckInfo checkInfo = new CheckInfo(checkInfoList[0], checkInfoList[1], checkInfoList[2],
                checkInfoList[3]);
            // 设置 文件中  content 的内容
            List<CheckContent> checkContent = new List<CheckContent>();
            for (int i=0;i< checkContentList.Count(); i+=3)
            {
                checkContent.Add(new CheckContent(checkContentList[i], checkContentList[i+1],
                    checkContentList[i+2]));
            }
            // 设置 文件中  checkerInfo 的内容
            List<CheckerInfo> checkerInfo = new List<CheckerInfo>();
            for (int i = 0; i < checkerInfoList.Count(); i += 6)
            {
                checkerInfo.Add(new CheckerInfo(checkerInfoList[i], checkerInfoList[i + 1],
                    checkerInfoList[i + 2], checkerInfoList[i + 3], checkerInfoList[i + 4],
                    checkerInfoList[i + 5]));
            }
            return new Check(checkInfo, checkContent, checkerInfo);
        }

        // 根据类生成对应的post信息
        public static Dictionary<string, string> getDictionary(Check check)
        {
            Dictionary<string, string> dictionary = new Dictionary<string, string>();
            StringBuilder edit = new StringBuilder("");
            StringBuilder chec = new StringBuilder("");
            string level = "0";
            dictionary.Add("fileName", check.checkInfo.fileName);
            dictionary.Add("type", check.checkInfo.type);
            dictionary.Add("group", check.checkInfo.group);
            dictionary.Add("number", check.checkInfo.number);

            
            for (int i = 0; i < check.checkContent.Count(); i++)
            {
                edit.Append(check.checkContent[i].edit);
                dictionary.Add(check.checkContent[i].name, check.checkContent[i].status);
            }
            dictionary.Add("checkEdit", edit.ToString());

            edit = new StringBuilder("");
            for (int i = 0; i < check.checkerInfo.Count(); i++)
            {
                edit.Append(check.checkerInfo[i].edit);
                chec.Append(check.checkerInfo[i].check);
                if(check.checkerInfo[i].check!=null && check.checkerInfo[i].check.Equals("1"))
                {
                    level = check.checkerInfo[i].level;
                }
                dictionary.Add(name[i], check.checkerInfo[i].name);
                dictionary.Add(date[i], check.checkerInfo[i].date);
                dictionary.Add(comments[i], check.checkerInfo[i].comments);
            }
            dictionary.Add("checkerEdit", edit.ToString());
            dictionary.Add("check", chec.ToString());
            dictionary.Add("level", level);

            return dictionary;
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
