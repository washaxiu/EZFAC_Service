using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EZFAC_Service.model
{
    class CheckRecord
    {
        private string fileName { get; set; }
        private string type { get; set; }
        private string group { get; set; }
        private string number { get; set; }
        private string temp1 { get; set; }
        private string temp2 { get; set; }
        private string temp3 { get; set; }
        private string loop1 { get; set; }
        private string loop2 { get; set; }
        private string loop3 { get; set; }
        private string select1 { get; set; }
        private string plat1 { get; set; }
        private string status { get; set; }
        private string edit { get; set; }
        private List<CheckerInfo> checkerInfo { get; set; }
    }
}
