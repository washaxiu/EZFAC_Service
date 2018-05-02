using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EZFAC_Service.model
{
    class CheckContent
    {
        public CheckContent() { }

        public CheckContent(string name,string status,string edit)
        {
            this.name = name;
            this.status = status;
            this.edit = edit;

        }

        private string name { get; set; }
        private string status { get; set; }
        private string edit { get; set; }
    }
}
