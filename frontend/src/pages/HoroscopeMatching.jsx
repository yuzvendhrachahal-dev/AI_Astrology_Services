import { useState } from "react";
import { generateMatchReport } from "../api/compatibilityApi";

export default function HoroscopeMatching() {

  const [form, setForm] = useState({
    groom_name: "",
    groom_dob: "",
    groom_time: "",
    groom_location: "",

    bride_name: "",
    bride_dob: "",
    bride_time: "",
    bride_location: "",
  });

  const [report, setReport] = useState(null);

  const submitForm = async () => {
    try {

      const result =
        await generateMatchReport(form);

      console.log(result);

      setReport(result.report);

    } catch (err) {
      console.error(err);
    }
  };

  const rows = [
    "Dhina",
    "Gana",
    "Mahendra",
    "StreeDeerga",
    "Yoni",
    "Rasi",
    "Rasiyathipaty",
    "Vasya",
    "Rajju",
    "Nadi",
  ];

  return (
    <div className="container">

      <h1>
        Horoscope Matching
      </h1>

      <h2>Groom Details</h2>

      <input
        placeholder="Enter Groom Name"
        onChange={(e) =>
          setForm({
            ...form,
            groom_name: e.target.value,
          })
        }
      />

      <input
        type="date"
        onChange={(e) =>
          setForm({
            ...form,
            groom_dob: e.target.value,
          })
        }
      />

      <input
        type="time"
        onChange={(e) =>
          setForm({
            ...form,
            groom_time: e.target.value,
          })
        }
      />

      <input
        placeholder="e.g Chennai, Tamil Nadu, India"
        onChange={(e) =>
          setForm({
            ...form,
            groom_location: e.target.value,
          })
        }
      />

      <h2>Bride Details</h2>

      <input
        placeholder="Enter Bride Name"
        onChange={(e) =>
          setForm({
            ...form,
            bride_name: e.target.value,
          })
        }
      />

      <input
        type="date"
        onChange={(e) =>
          setForm({
            ...form,
            bride_dob: e.target.value,
          })
        }
      />

      <input
        type="time"
        onChange={(e) =>
          setForm({
            ...form,
            bride_time: e.target.value,
          })
        }
      />

      <input
        placeholder="e.g Chennai, Tamil Nadu, India"
        onChange={(e) =>
          setForm({
            ...form,
            bride_location: e.target.value,
          })
        }
      />

      <button onClick={submitForm}>
        Generate Match Report
      </button>

      {report && (
        <div className="report-container">

          <h2>Horoscope Matching Report</h2>

          <div className="header-cards">

            <div className="card">
              <h3>Groom</h3>

              <p>
                Nakshatra:
                {" "}
                {report.BoyNakshatra}
              </p>

              <p>
                Zodiac:
                {" "}
                {report.BoyZodiac}
              </p>

              <p>
                Lagna:
                {" "}
                {report.BoyLagna}
              </p>
            </div>

            <div className="card">
              <h3>Bride</h3>

              <p>
                Nakshatra:
                {" "}
                {report.GirlNakshatra}
              </p>

              <p>
                Zodiac:
                {" "}
                {report.GirlZodiac}
              </p>

              <p>
                Lagna:
                {" "}
                {report.GirlLagna}
              </p>
            </div>

          </div>

          <table>

            <thead>
              <tr>
                <th>Compatibility</th>
                <th>Description</th>
                <th>Status</th>
              </tr>
            </thead>

            <tbody>

              {rows.map((row) => {

                const item =
                  report[row];

                if (!item) return null;

                return (
                  <tr key={row}>
                    <td>
                      {item.CompatibilityName}
                    </td>

                    <td>
                      {item.StatusDescription}
                    </td>

                    <td>
                      {item.Status}
                    </td>
                  </tr>
                );
              })}

            </tbody>

          </table>

          <div className="summary">

            <h3>
              Score:
              {" "}
              {report.TotalValue}
            </h3>

            <p>
              {report.Summary}
            </p>

          </div>

        </div>
      )}

    </div>
  );
}