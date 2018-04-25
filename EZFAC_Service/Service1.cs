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

        public Service1()
        {
            InitializeComponent();
            timer1 = new Timer();
            timer1.Interval = 5000;
            timer1.Elapsed += new ElapsedEventHandler(timer1_Elapsed);
            timer1.Enabled = true;
        }

        protected override void OnStart(string[] args)
        {
            timer1.Start();
            this.WriteLog("【服务启动】");
        }

        protected override void OnStop()
        {
            timer1.Stop();
            this.WriteLog("【服务停止】");
        }

        private void timer1_Elapsed(object sender, ElapsedEventArgs e)
        {
            //时间控件定时任务
            // 1. 访问接口
            // 2. 记录日志
            this.WriteLog(++count+" : 数据获取");
        }

        private void WriteLog(string msg)
        {
            //该日志文件会存在windows服务程序目录下
            string path = @"d:\log\";
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


        private string GetReport(string RequestPara, string Url)
        {
            RequestPara = RequestPara.IndexOf('?') > -1 ? (RequestPara) : ("?" + RequestPara);
            WebRequest hr = HttpWebRequest.Create(Url + RequestPara);
            byte[] buf = System.Text.Encoding.GetEncoding("utf-8").GetBytes(RequestPara);
            hr.Method = "GET";
            try
            {
                System.Net.WebResponse response = hr.GetResponse();
                StreamReader reader = new StreamReader(response.GetResponseStream(), Encoding.GetEncoding("utf-8"));
                string ReturnVal = reader.ReadToEnd();
                reader.Close();
                response.Close();
                return ReturnVal;
            }
            catch (System.Net.WebException wex)
            {
                string error_info = "WebException=" + wex.ToString() + ",wex.Status=" + wex.Status;
                return error_info;
            }
        }
    }
}
