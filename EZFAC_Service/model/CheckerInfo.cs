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
        private string name { get; set; }
        private string level { get; set; }
        private string check { get; set; }
        private string edit { get; set; }
        private string date { get; set; }
        private string comments { get; set; }
    }
}
