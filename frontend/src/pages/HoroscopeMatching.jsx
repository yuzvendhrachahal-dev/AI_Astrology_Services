import { useState } from "react";

import { generateMatchReport } from "../api/compatibilityApi";
export default function HoroscopeMatching() {

 const [form,setForm] =
 useState({

   groom_name:"",
   groom_dob:"",
   groom_time:"",
   groom_country:"",
   groom_location:"",

   bride_name:"",
   bride_dob:"",
   bride_time:"",
   bride_country:"",
   bride_location:""
 });

 const [report,setReport] =
 useState("");

 const submitForm =
 async () => {

   const result =
   await generateMatchReport(
     form
   );

   setReport(
     result.report
   );
 };

 return (

 <div className="container">

   <h1>
   AI Horoscope Matching
   </h1>

   <h2>Groom Details</h2>

   <input
   placeholder="Name"

   onChange={(e)=>

   setForm({
   ...form,
   groom_name:e.target.value
   })

   }
   />

   <input
   type="date"

   onChange={(e)=>

   setForm({
   ...form,
   groom_dob:e.target.value
   })

   }
   />

   <input
   type="time"

   onChange={(e)=>

   setForm({
   ...form,
   groom_time:e.target.value
   })

   }
   />

   <input
   placeholder="Country"

   onChange={(e)=>

   setForm({
   ...form,
   groom_country:e.target.value
   })

   }
   />

   <input
   placeholder="Birth Location"

   onChange={(e)=>

   setForm({
   ...form,
   groom_location:e.target.value
   })

   }
   />

   <h2>Bride Details</h2>

   <input
   placeholder="Name"

   onChange={(e)=>

   setForm({
   ...form,
   bride_name:e.target.value
   })

   }
   />

   <input
   type="date"

   onChange={(e)=>

   setForm({
   ...form,
   bride_dob:e.target.value
   })

   }
   />

   <input
   type="time"

   onChange={(e)=>

   setForm({
   ...form,
   bride_time:e.target.value
   })

   }
   />

   <input
   placeholder="Country"

   onChange={(e)=>

   setForm({
   ...form,
   bride_country:e.target.value
   })

   }
   />

   <input
   placeholder="Birth Location"

   onChange={(e)=>

   setForm({
   ...form,
   bride_location:e.target.value
   })

   }
   />

   <button
   onClick={submitForm}
   >
     Generate Match Report
   </button>

   <div
   className="report-box"
   >
     <pre>
       {report}
     </pre>
   </div>

 </div>

 );
}