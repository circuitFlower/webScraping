from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import socket
import sys

from tensorflow.python.platform import app

os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "cpp"
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSIN"]="2"

FLAGS = None

ORIGIN_ARGV = sys.argv
IS_KERNEL = len(sys.argv) >1 and sys.argv[1] == "kernel"

def main(unused_argv):
	sys.argv = ORIG_ARGV

	if not IS_KERNEL:
		sys.argv = [sys.argv[0]]
		from IPython.html.notebookapp import NotebookApp
		notebookapp = NotebookApp.instance()
		notebookapp.open_browser = True

		if FLAGS.password:
			from IPython.lib import passwd
			notebook.ip="0.0.0.0"
			notebook.password=passwd(FLAGS.password)
		else:
			print("\nNo password specified: Notebook server will only be available"
				" on the local machine.\n")
		notebookapp.initialize(argv=["--notebook-dir", FLAGS.notebook_dir])

		if notebookapp.ip == "0.0.0.0":
			proto = "https" if notebookapp.certfile else "http"
			url = "%s://%s:%d%s" % (proto, socket.gethostname(), notebookapp.port, 
					notebookapp.base_project_url)
			print("\nNotebook server will be publicly available at: %s\n" % url)

		notebookapp.start()
		return
	sys.argv = ([sys.argv[0]] +
		    [z for z in sys.argv[1:] if not z.startswith("--flagfile")])
	from IPython.kernel.zmq.kernelapp import IPKernelApp
	kernelapp = IPKernelApp.instance()
	kernelapp.initialize()

	ipshell = kernelapp.shell
	ipshell.enable_matplotlib("inline")

	kernelapp.start()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"--password",
		type=str,
		default=None,
		help="""Password""")
	parser.add_argument(
		"--notebook_dir",
		type=str,
		default="experimental/brain/notebooks",
		help="root location where to store notebooks")
	if IS_KERNEL:
		sys.argv = (
			[sys.argv[0]] + [x for x in sys.argv[1:] if x.startswith("--flagfile")])

	FLAGS, unparsed = parser.parse_known_args()
	app.run(main=main, argv=[sys.argv[0]] + unparsed)
