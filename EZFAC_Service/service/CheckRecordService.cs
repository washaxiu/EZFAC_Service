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
            DirectoryInfo dir = new DirectoryInfo(@ditPath);
            FileInfo[] files = dir.GetFiles();
            StreamReader myStreamReader = null;
            string content = null;
            string[] str = null;
            for (int i = 0; i < files.Count(); i++)
            {
                myStreamReader = new StreamReader(files[i].FullName);    // 读取文件数据
                content = myStreamReader.ReadToEnd().Replace("   ", "").Replace("\"", "").Replace(",", "");
                str = content.Split('\n');
                for (int j = 0; j < str.Count(); j++)
                {
                    if (str[i].IndexOf(":") != -1)
                    {
                        string[] st = str[i].Trim().Split(':');

                        if (st[1].Equals("["))
                        {
                            //  Console.WriteLine("%%%%%%%%%%%%%%%%");
                        }
                        else
                        {
                            if (st[1].Equals(""))
                            {
                                Console.WriteLine("########");
                            }
                            Console.WriteLine(st[0] + "---->" + st[1]);
                        }
                        // else Console.WriteLine(str[i] + "-------", + st.Count());
                    }
                }
            }
        }
    }
}
