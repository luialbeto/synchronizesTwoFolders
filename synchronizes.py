import os
import shutil
import time
import logging
import argparse


def setup_logging(log_file):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )


def sync_folders(source, replica):
    for src_dir, dirs, files in os.walk(source):
        rel_path = os.path.relpath(src_dir, source)
        dest_dir = os.path.join(replica, rel_path)

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            logging.info(f"Directory created: {dest_dir}")

        for file in files:
            src_file = os.path.join(src_dir, file)
            dest_file = os.path.join(dest_dir, file)
            if not os.path.exists(dest_file) or os.path.getmtime(src_file) > os.path.getmtime(dest_file):
                shutil.copy2(src_file, dest_file)
                logging.info(f"File copied: {src_file} to {dest_file}")


def synchronize_folders(source, replica, interval, log_file):
    setup_logging(log_file)
    logging.info("Starting synchronization...")

    while True:
        sync_folders(source, replica)
        logging.info("Synchronization complete. Waiting for next interval...")
        time.sleep(interval)


def main():
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument('source', help="Path to the source folder")
    parser.add_argument('replica', help="Path to the replica folder")
    parser.add_argument('interval', type=int,
                        help="Synchronization interval in seconds")
    parser.add_argument('log_file', help="Path to the log file")

    args = parser.parse_args()
    synchronize_folders(args.source, args.replica,
                        args.interval, args.log_file)


if __name__ == "__main__":
    main()
