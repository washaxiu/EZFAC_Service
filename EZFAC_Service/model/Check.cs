using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EZFAC_Service.model
{
    class Check
    {
        public Check() { }

        public Check(CheckInfo checkInfo, List<CheckContent> checkContent,
            List<CheckerInfo> checkerInfo)
        {
            this.checkInfo = checkInfo;
            this.checkContent = checkContent;
            this.checkerInfo = checkerInfo;
        }

        private CheckInfo checkInfo { get; set; }
        private List<CheckContent> checkContent { get; set; }
        private List<CheckerInfo> checkerInfo { get; set; }
    }
}
