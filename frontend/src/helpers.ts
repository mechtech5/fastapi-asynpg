// import { debounce } from "lodash";
// import { format } from "date-fns";
// import { setReportData } from "@/store/slices/report.slice";
// import { toast } from "react-toastify";
// import { getFormattedDate } from "@/components/timeUtils";

// export const debouncedSave = debounce((dispatch, key, value) => {
//   dispatch(setReportData({ key, value }));
// }, 200);

// export const validateReporterDetails = ({
//   first_name,
//   last_name,
//   phone,
//   email,
// }) => {
//   // validate all fields are filled and valid
//   if (!first_name || !last_name || !phone || !email) {
//     return false;
//   }
//   return true;
// };

// export const prepareOptions = (data, category) => {
//   const temp = [];
//   data.forEach((record) => {
//     const index = temp.find((item) => {
//       if (category === "created_at") {
//         return (
//           item?.label ===
//           format(new Date(record[category]?.split(".")[0]), "dd-MM-yyyy")
//         );
//       } else {
//         return (
//           JSON.stringify(item?.label)?.toLowerCase() ===
//           JSON.stringify(record[category])?.toLowerCase()
//         );
//       }
//     });
//     if (!index || temp?.length === 0)
//       temp?.push({
//         label:
//           category === "created_at"
//             ? format(new Date(record[category]?.split(".")[0]), "dd-MM-yyyy")
//             : record[category],
//         value: record[category],
//       });
//   });
//   // sort options alphabetically and then return
//   if (category === "report_about") {
//     return temp;
//   } else if (category === "created_at") {
//     return temp?.sort();
//   } else {
//     return temp?.sort((a, b) => {
//       if (
//         a.label === null ||
//         b.label === null ||
//         a.label?.toLowerCase() < b.label?.toLowerCase()
//       ) {
//         return -1;
//       }
//       if (a.label?.toLowerCase() > b.label?.toLowerCase()) {
//         return 1;
//       }
//       return 0;
//     });
//   }
// };

// export const notify = (message, type) =>
//   toast(message, {
//     position: "top-right",
//     autoClose: 2000,
//     hideProgressBar: false,
//     closeOnClick: true,
//     pauseOnHover: true,
//     draggable: true,
//     progress: undefined,
//     theme: "dark",
//     type,
//   });

// export const getDutchDST = (data) => {
//   const date = new Date(data);
//   const year = date.getFullYear();
//   const dstStart = new Date(year, 2, 31); // Last Sunday in March
//   dstStart.setDate(dstStart.getDate() - dstStart.getDay());
//   const dstEnd = new Date(year, 9, 31); // Last Sunday in October
//   dstEnd.setDate(dstEnd.getDate() - dstEnd.getDay());

//   if (date >= dstStart && date < dstEnd) {
//     return date;
//   } else {
//     const adjustedDate = new Date(date.getTime() + 60 * 60 * 1000); // Adding 1 hour in milliseconds
//     return adjustedDate;
//   }
// };

// export const sanitizeData = (key, value) => {
//   if (typeof value === "string") {
//     if (["created_at"].includes(key)) {
//       value = getFormattedDate(getDutchDST(value));
//     }
//     // Remove or replace dangerous characters
//     value = value.replace(/[\+\-=()]/g, "");

//     // Validate data format
//     if (/^[\d\.]+$/.test(value)) {
//       // If the value is numeric, make sure it doesn't start with an equal sign
//       if (value.charAt(0) === "=") {
//         value = "'" + value;
//       }
//     } else if (/^=/.test(value)) {
//       // If the value starts with an equal sign, prefix it with an apostrophe
//       value = "'" + value;
//     }

//     // Limit cell content length
//     const maxLength = 32767; // Adjust as needed
//     if (value.length > maxLength) {
//       value = value.substring(0, maxLength);
//     }

//     // Implement your data sanitization logic here
//     // For simplicity, this example just replaces double quotes with single quotes
//     value?.replace(/"/g, "'");
//   }

//   return value;
// };

// export const reverseDate = (data) =>
//   data ? data?.split("/")?.reverse()?.join("/") : "";
