using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EZFAC_Service.model
{
    class CheckerInfo
    {
        public CheckerInfo() { }

        public CheckerInfo(string name, string level, string check,
              string edit, string date, string comments)
        {
            this.name = name;
            this.level = level;
            this.check = check;
            this.edit = edit;
            this.date = date;
            this.comments = comments;
        }
        public string name { get; set; }
        public string level { get; set; }
        public string check { get; set; }
        public string edit { get; set; }
        public string date { get; set; }
        public string comments { get; set; }
    }
}
