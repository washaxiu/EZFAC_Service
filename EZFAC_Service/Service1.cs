using EZFAC_Service.Common;
using EZFAC_Service.service;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.ServiceProcess;
using System.Text;
using System.Threading.Tasks;
using System.Timers;

namespace EZFAC_Service
{
    public partial class Service1 : ServiceBase
    {
        private int count = 0;
        private Timer timer1;
        private WebHandle wenHandle;
        public string sourcePath;
        public static string sourceUrl = "http://192.168.2.110:8800";
        // public static string checkRecordUrl = "http://192.168.80.254:8800/add-checkRecord";


        public Service1()
        {
            InitializeComponent();
            timer1 = new Timer();
            wenHandle = new WebHandle();
            timer1.Interval = 1000*10;
            timer1.Elapsed += new ElapsedEventHandler(timer1_Elapsed);
            timer1.Enabled = true;

            try
            {
                string path = "C:/Users/", dirPath = null;
                DirectoryInfo dir = new DirectoryInfo(@path);

                DirectoryInfo[] childDir = dir.GetDirectories();
                FileInfo file = null;
                for (int i = 0; i < childDir.Count(); i++)
                {
                    dirPath = childDir[i].FullName.Replace("\\", "/") + "/Pictures/user.json";
                    file = new FileInfo(@dirPath);
                    if (file.Exists)
                    {
                        sourcePath = childDir[i].FullName.Replace("\\", "/") + "/Pictures";
                        break;
                    }
                }
            }
            catch (Exception ex)
            {
                count = 1;
            }
        }

        protected override void OnStart(string[] args)
        {
            
            timer1.Start();
          //  this.WriteLog("【服务启动】");
        }

        protected override void OnStop()
        {
            timer1.Stop();
          //  this.WriteLog("【服务停止】");
        }

        private void timer1_Elapsed(object sender, ElapsedEventArgs e)
        {
            //时间控件定时任务
            // 1. 访问接口
            // 2. 记录日志
            // this.WriteLog(++count+" : 数据获取");
            //    string path = AppDomain.CurrentDomain.BaseDirectory;

            //  WriteLog("图片目录:" + Environment.GetFolderPath(Environment.SpecialFolder.MyPictures));

            //    string checkRecordDir = dirPath + "/CheckRecord";
            //   WriteLog(sb.ToString());  
            CommonUtils.handleFileDate(sourcePath+ "/CheckRecord", sourceUrl + "/add-checkRecord");
            CommonUtils.handleFileDate(sourcePath + "/DailyCheckMorning", sourceUrl+ "/add-DailyCheckMorning");
            CommonUtils.handleFileDate(sourcePath + "/DailyCheckNoon", sourceUrl+ "/add-DailyCheckNoon"); 
            CommonUtils.handleFileDate(sourcePath + "/MaintenanceLog", sourceUrl+ "/add-MaintenanceLog");
            CommonUtils.handleFileDate(sourcePath + "/SemiFinishedCheck", sourceUrl+ "/add-SemiFinishCheck");
            CommonUtils.handleFileDate(sourcePath + "/YZGCMonthRecord", sourceUrl+ "/add-YZGCMonthRecord");
            
        }

        private void WriteLog(string msg)
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

        public static string testGet()
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create("http://192.168.80.254:8800/get-line-list");
            // 为URL添加cookie
            request.CookieContainer = new CookieContainer();
            request.Method = "GET";
            request.ContentType = "text/html;charset=UTF-8";
            request.UserAgent = null;
            request.Timeout = 10000;

            HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            Stream myResponseStream = response.GetResponseStream();
            StreamReader myStreamReader = new StreamReader(myResponseStream, Encoding.GetEncoding("utf-8"));
            string retString = myStreamReader.ReadToEnd();
            myStreamReader.Close();
            myResponseStream.Close();

            return retString;
        }

    }
}
