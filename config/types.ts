// types.ts
export enum UserRole {
  ADMIN = 'admin',
  MODERATOR = 'moderator',
  USER = 'user'
}

export interface User {
  id: number;
  username: string;
  email: string;
  role: UserRole;
  createdAt: Date;
  updatedAt: Date;
}

export interface DashboardStats {
  totalUsers: number;
  activeUsers: number;
  newUserCount: number;
}

export interface UserDashboardResponse {
  user: User;
  stats: DashboardStats;
}