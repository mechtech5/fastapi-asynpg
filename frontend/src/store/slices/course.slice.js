export const createCourseSlice = (set) => ({
  courses: 0,
  increase: (by) => set((state) => ({ courses: state.courses + by })),
});
