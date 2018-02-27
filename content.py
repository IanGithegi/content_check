# List All files within a folder. To much a certain criteria
import os
import click

"""
    This is a script that is to check on the content and verify each file for each content meets the Moja Content Platform- Simiti

"""
source_dir = False

@click.command()
@click.option('--path', default='.', help='Where the Content is stored or placed.')
def content_count(path):
    global source_dir
    source_dir = path

    print("----------Show Files and count on Each directory")
    print 'Number of Folders is %d' % len(os.listdir(path))
    bdfiles = open(path+"/bdfiles.txt", "w")

    for root, dir, filenames in os.walk(path):
        count = 0
        dir = [d for d in dir if not d[0] == '.']
        filenames = [f for f in filenames if not f[0] == '.']
        click.echo('Directory: is %s' % root)
        for f in filenames:
                click.echo('\t%s' % f)
                count += 1
        if (count > 4):
            print 'Check bdfiles.txt for Results'
            print >> bdfiles, '%d Extra File(s) in %s. Remove Files' % (count-4, path)
        else:
            click.echo(count == 4)


def files_verify():
    click.echo("Checks if Each file provided meets every specifictaions.")
    """
    Split each file and work on it individually then move to the next file till all files are cleared in each Folder

    """
    poster_matches = []
    for p in inter_matching(path, re.compile(r'poster.*$').match):
        poster_matches.append(p)
    thumbnail_matches = []
    for thumb in inter_matching(path, re.compile(r'thumbnail.*$').match):
        thumbnail_matches.append(thumb)
    metadata_matches = []
    for mt_data in inter_matching(path, re.compile(r'))


if __name__ == '__main__':
    content_count()
