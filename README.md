# m3u_modifier

Modifies m3u for Jellyfin + Schedules Direct compatibility

## Features:

- Sets channel number to 0 -> Fixes Jellyfin showing channel numbers in name so
  SchedulesDirect can match based on channel names

## Usage:
1. Pull the repo
2. `cd m3u_modifier`
3. Create .env file and add the source m3u url like `M3U_URL=http://localhost/channels.m3u` to it
4. On first run `docker-compose up -d` or to update `docker-compose up -d --build`
