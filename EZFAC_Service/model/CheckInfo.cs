using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EZFAC_Service.model
{
    class CheckInfo
    {
        public CheckInfo() { }

        public CheckInfo(string fileName,string type,string group,string number)
        {
            this.fileName = fileName;
            this.type = type;
            this.group = group;
            this.number = number;
        }

        private string fileName { get; set; }
        private string type { get; set; }
        private string group { get; set; }
        private string number { get; set; }
    }
}
