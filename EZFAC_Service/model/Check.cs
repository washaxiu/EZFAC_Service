﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EZFAC_Service.model
{
    class Check
    {
        public Check() { }

        public Check(Dictionary<string, string> checkInfo, List<CheckContent> checkContent,
            List<CheckerInfo> checkerInfo)
        {
            this.checkInfo = checkInfo;
            this.checkContent = checkContent;
            this.checkerInfo = checkerInfo;
        }

        public Dictionary<string,string> checkInfo { get; set; }
        public List<CheckContent> checkContent { get; set; }
        public List<CheckerInfo> checkerInfo { get; set; }
    }
}
